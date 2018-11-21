import json
import requests
import os
import re
try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace

'''
'---------------------------------------------------------------------------------------------------
' zCymatix NLU service client API
'---------------------------------------------------------------------------------------------------
'''
class zCymatix:

    '''
    ' Ctor
    '''
    def __init__( self, user_name, user_pwd, url = None ):
        self.m_url = url if url else 'https://nlp2.zcymatix.com'
        self.m_user_name = user_name
        self.m_user_pwd = user_pwd
        self.m_ret_msg_cleaner = re.compile( r"<.+?>" )

    '''
    ' Sign in to zCymatix NLU service. Previous session id should be provided to access
    ' user instance of the application stored after first login.
    '
    ' Return:
    '   session_id on success. Keep it secret
    '   None on error
    '''
    def login( self, prev_session_id = None ):
        data = {
            'user_id' : self.m_user_name,
            'user_pwd': self.m_user_pwd,
            'zcmd': 'login' }
        if prev_session_id:
            data.update( { 'session_id': prev_session_id } )

        resp = zCymatix.http_post( self.m_url, data )
        return self.return_value( resp, expected_code = 200 )

    '''
    ' Sign out from zCymatix NLU service. NOTE! In practice, logout is NOT required unless
    ' application instance is not needed any longer. There may be
    ' user instance persistant data associated with the session id. See memory types
    ' in zCymatix NLU service: https://github.com/vladbph/zcymatix
    '''
    def logout( self, session_id ):
        if session_id:
            data = {
                'session_id' : session_id,
                'zcmd': 'logout' }
            resp = zCymatix.http_post( self.m_url, data )
        else:
            resp = None
        return self.return_value( resp, expected_code = 0 )

    '''
    ' Upload a project to the backend
    ' Return:
    '   project_id Keep it secret.
    '   None on error
    '''
    def upload_project( self, session_id, project_folder ):
        if not session_id or not project_folder:
            return 100, 'Invalid parameters'

        data = {
            'session_id': session_id,
            'zcmd': 'upload' }

        project_folder = os.path.normpath( project_folder )
        project_name = os.path.basename( project_folder )

        filenames = zCymatix._dir( project_folder )
        if not filenames:
            return 100, 'Project folder {} is invalid'.format( project_folder )
        else:
            print 'Uploading {}'.format( project_folder )
        file_handles = [ open( filename, 'rb' ) for filename in filenames ]
        filenames_only = [ filename[ len( project_folder ) + len( os.sep ) : ] for filename in filenames ]
        project_files = [ zCymatix._join( project_name, filename ) for filename in filenames_only ]
        files = [ ( 'file', ( project_files[ i ], file_handles[ i ] ) ) for i, _ in enumerate( filenames ) ]

        resp = zCymatix.http_post( self.m_url, data = data, files = files )

        def on_success( resp ):
            all_projects = zCymatix.json_to_obj( resp.msg )
            return zCymatix.get_config( all_projects, project_name, 'project_id' )

        return self.return_value( resp, expected_code = 207, msg = 'success', on_success = on_success )

    '''
    ' Train uploaded project
    '''
    def train( self, session_id, project_id ):
        if not session_id or not project_id:
            return 100, 'Invalid parameters'

        data = {
            'session_id': session_id,
            'project_id': project_id,
            'exec_mode': 0,
            'zcmd': 'launch',
            'production': 0 }

        resp = zCymatix.http_post( self.m_url, data )
        return self.return_value( resp, expected_code = 200, msg = 'success' )

    '''
    ' Launch uploaded and trained project for prediction
    ' Project can be started in either:
    '   1. Test mode (production_mode = False)
    '   2. Production mode (production_mode = False)
    ' Test and production instances are independent.
    '''
    def start( self, session_id, project_id, production = False ):
        if not session_id or not project_id:
            return 100, 'Invalid parameters'
        data = {
            'session_id': session_id,
            'project_id' : project_id }
        data.update( { 'zcmd': 'deploy' } ) if production else data.update( { 'zcmd': 'launch', 'production': 0 } )
        expected_code = 209 if production else 200

        resp = zCymatix.http_post( self.m_url, data )
        return self.return_value( resp, expected_code = expected_code, msg = 'success' )

    '''
    ' Stop launched test/production project
    '''
    def stop( self, session_id, project_id, production = False ):
        if not session_id or not project_id:
            return 100, 'Invalid parameters'
        data = {
            'session_id': session_id,
            'project_id' : project_id,
            'production': production,
            'zcmd': 'stop' }

        resp = zCymatix.http_post( self.m_url, data )
        return self.return_value( resp, expected_code = 204, msg = 'success' )

    '''
    ' Delete a project. Cannot be recovered.
    '''
    def delete_project( self, session_id, project_id ):
        if not project_id:
            return 100, 'Invalid parameters'
        data = {
            'session_id': session_id,
            'project_id' : project_id,
            'zcmd': 'delete' }

        resp = zCymatix.http_post( self.m_url, data )
        return self.return_value( resp, expected_code = 206, msg = 'success' )

    '''
    ' Make an inference
    '''
    def infer( self, session_id, project_id, utterance, production = False ):
        if not session_id or not utterance:
            return 100, 'Invalid parameters'
        data = {
            'session_id': session_id,
            'project_id': project_id,
            'production': production,
            'query': utterance,
            'zcmd': 'infer' }

        resp = zCymatix.http_post( self.m_url, data )
        return self.return_value( resp, expected_code = 201 )

    '''
    ' Get all projects list
    '''
    def project_list( self, session_id ):
        if not session_id:
            return 100, 'Invalid parameters'
        data = {
            'session_id': session_id,
            'zcmd': 'get_projects' }

        resp = zCymatix.http_post( self.m_url, data )
        return self.return_value( resp, expected_code = 208 )

    '''
    ' Clear history of the current project for the session
    '''
    def clear_history( self, session_id, production = False ):
        if not session_id:
            return 100, 'Invalid parameters'
        data = {
            'session_id': session_id,
            'production': production,
            'zcmd': 'clear_history' }

        resp = zCymatix.http_post( self.m_url, data )
        return self.return_value( resp, expected_code = 0 )

    '''
    ' Check backend responce and return value to user
    '''
    def return_value( self, resp, expected_code = 0, msg = None, on_success = None ):
        resp = zCymatix.decode_resp( resp )
        if resp:
            if resp.code == expected_code:
                if on_success:
                    msg = on_success( resp )
                if not msg:
                    msg = resp.msg
                if msg and isinstance( msg, str ):
                    msg = self.m_ret_msg_cleaner.sub( '', msg )
                return 0, msg
            else:
                if resp.msg:
                    resp.msg = self.m_ret_msg_cleaner.sub( '', resp.msg )
                return resp.code, resp.msg
        return 100, 'Unknown error'

    '''
    ' Get all file names in the folder(s)
    '''
    @staticmethod
    def _dir( folder_name ):
        file_names = []
        if isinstance( folder_name, list ):
            for folder in folder_name:
                folder = os.path.normpath( folder )
                extra = zCymatix._dir( folder )
                if extra:
                    file_names.extend( extra )
        else:
            folder_name = os.path.normpath( folder_name )
            for folder, _, files in os.walk( folder_name ):
                for file_name in files:
                    file_names.append( zCymatix._join( folder, file_name ) )
        return file_names if file_names is not None and file_names else None

    '''
    ' Join path
    '''
    @staticmethod
    def _join( folder, file_name ):
        if not file_name:
            return folder
        if isinstance( file_name, list ):
            return [ zCymatix._join( folder, name ) for name in file_name ]
        file_name = file_name.strip( os.sep )
        folder = folder.strip( os.sep )
        return os.path.normpath( os.path.join( folder, file_name ) )

    '''
    ' POST an object {'key':'value'} to the URL
    '''
    @staticmethod
    def http_post( url, data = {}, files = None ):
        try:
            if files:
                r = requests.post( url, data = data, files = files )
            else:
                r = requests.post( url, data = data )
            return r.text
        except:
            return None

    '''
    ' Convert dict or Namespace to pretty JSON string
    '''
    @staticmethod
    def to_json( obj, sort_keys = True ):
        if obj is None:
            return None
        else:
            if isinstance( obj, Namespace ):
                obj = vars( obj )
            return json.dumps( obj, indent = 4, sort_keys = sort_keys )

    '''
    ' Convert JSON string to python dict
    '''
    @staticmethod
    def json_to_obj( json_str ):
        try:
            return json.loads( json_str )
        except:
            return None

    '''
    ' Convert either: json/dict/string to Namespace
    '''
    @staticmethod
    def to_namespace( obj ):
        if obj is not None:
            if isinstance( obj, Namespace ):
                return obj
            elif isinstance( obj, dict ):
                return Namespace( **obj )
            else:
                return zCymatix.to_namespace( zCymatix.json_to_obj( obj ) )
        else:
            return None

    '''
    ' Check if backend response is valid
    '''
    @staticmethod
    def decode_resp( resp ):
        resp = zCymatix.to_namespace( resp )
        if resp and hasattr( resp, 'code' ) and hasattr( resp, 'msg' ):
            return resp
        return None

    '''
    ' Get project configuration or specific parameter
    '''
    @staticmethod
    def get_config( all_projects, project_name, param_name = None ):
        if all_projects and all_projects.has_key( project_name ):
            project_config = all_projects[ project_name ]
            if param_name:
                if project_config and project_config.has_key( param_name ):
                    param_value = project_config[ param_name ]
                    return param_value
            else:
                return project_config
        return None
