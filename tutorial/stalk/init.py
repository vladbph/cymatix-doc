//--------------------------------------------------------------------------------------------------
// The purpose of this code is to read user data very first time application instance starts
//--------------------------------------------------------------------------------------------------
.vars
    s_init_done = False
    s_user_data_file = 'user.json'

.gate2
    if not s_init_done:
        data = read( z_sid, s_user_data_file, shared = False )
        if data:
            s_user = to_namespace( data )
            print s_user
        s_init_done = True
//--------------------------------------------------------------------------------------------------
