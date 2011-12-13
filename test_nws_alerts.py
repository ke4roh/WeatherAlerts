from nws_alerts import nws_alerts
import nagios_NWS_Alerts

# Some basic Nose tests.... 

#def test_imports():
    #from nws_alerts import nws_alerts
    #import nagios_NWS_Alerts
    
    
def test_alerts_objcreation():
    #from nws_alerts import nws_alerts
    alerts = nws_alerts.Alerts()
    
def test_same_objcreation():
    #from nws_alerts import nws_alerts
    same = nws_alerts.SameCodes()
    
    
def test_cap_objcreation():
    #from nws_alerts import nws_alerts
    cap = nws_alerts.CapAlertsFeed()
    
def test_cap_obj_reload():
    cap = nws_alerts.CapAlertsFeed(state='ID')
    cap.reload_alerts()

def test_samecodes_objcreation():
    #from nws_alerts import nws_alerts
    same = nws_alerts.SameCodes()
    
def test_samecodes_obj_reload():
    same = nws_alerts.SameCodes()
    same.reload()
    
def test_nagios_plugin():
    samecodes = '''016027,016001'''
    nagios_NWS_Alerts.loadalerts(samecodes)
    
def test_same_get_state():
    testcases = [('016027', 'ID'), 
                 ('047065', 'TN')]
    same = nws_alerts.SameCodes()
    for code, state in testcases:
        response = same.getstate(code)
        assert response == state
        
def test_same_get_scope():
    same = nws_alerts.SameCodes()
    testcases = [(['016027','047065'], 'US'),
                 (['016027','016001'], 'ID'),
                 (['016027'], 'ID')]
    for codes, scope in testcases:
        response = same.getfeedscope(codes)
        assert response == scope
    