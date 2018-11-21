from zcymatix import zCymatix

api = zCymatix( user_name = 'benchmark', user_pwd = 'benchmark', url = 'http2://nlp2.zcymatix.com' )

class Color:
    OkGreen = '\033[92m'
    Fail = '\033[91m'
    End = '\033[0m'

def print_ok( string ):
    string = '{}{}{}'.format( Color.OkGreen, string, Color.End )
    print string

def print_failed( string ):
    string = '{}{}{}'.format( Color.Fail, string, Color.End )
    print string

def login( ):
    error, session_id = api.login( )
    fprint = print_ok if not error else print_failed
    fprint( 'Session id: {}'.format( session_id ) )
    return session_id

def logout( session_id ):
    error, msg = api.logout( session_id )
    fprint = print_ok if not error else print_failed
    fprint( 'Logout: {}'.format( msg ) )
    return msg

def upload( session_id, project_folder ):
    error, project_id = api.upload_project( session_id, project_folder )
    fprint = print_ok if not error else print_failed
    fprint( 'Project id: {}'.format( project_id ) )
    return project_id

def train( session_id, project_id ):
    error, msg = api.train( session_id, project_id )
    fprint = print_ok if not error else print_failed
    fprint( 'Training: {}'.format( msg ) )
    return msg

def start( session_id, project_id, production = False ):
    error, msg = api.start( session_id, project_id, production = production )
    fprint = print_ok if not error else print_failed
    fprint( 'Project start. Production({}): {}'.format( production, msg ) )
    return msg

def stop( session_id, project_id, production = False ):
    error, msg = api.stop( session_id, project_id, production = production )
    fprint = print_ok if not error else print_failed
    fprint( 'Project stop. Production({}): {}'.format( production, msg ) )
    return msg

def infer( session_id, project_id, utterance, production = False ):
    error, msg = api.infer( session_id, project_id, utterance = utterance, production = production )
    fprint = print_ok if not error else print_failed
    fprint( 'Inference: {}'.format( msg ) )
    return msg

def delete_project( session_id, project_id ):
    error, msg = api.delete_project( session_id, project_id )
    fprint = print_ok if not error else print_failed
    fprint( 'Inference: {}'.format( msg ) )
    return msg

def project_list( session_id ):
    error, msg = api.project_list( session_id )
    fprint = print_ok if not error else print_failed
    fprint( 'Inference: {}'.format( msg ) )
    return msg

'''
' Main
'''
if __name__ == '__main__':
    session_id = login( )
    project_id = upload( session_id, '../../tutorial/hello' )
    train( session_id, project_id )
    # After training project has already been started in test mode
    # start( session_id, project_id )
    infer( session_id, project_id, 'hello' )
    logout( session_id )
