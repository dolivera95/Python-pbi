# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'MasterUser'

    # Workspace Id in which the report is present
    WORKSPACE_ID = 'bbdf7b14-87b6-4880-ab65-c254f371e131'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '222a4f4c-c0dd-4b88-a3a4-ff02409006ee'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '6a47a471-a160-4d51-ab00-72d507f3aa61'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = 'aeb91e39-588e-4e97-b301-641266d6ccd9'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = '6y.v4-i3Y5V_o25~X3.XSY6SUJF0233x2H'
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'servicioBIRepsol@itsmart.pe'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = '#TAMpowerbi202106'