import pandas as pd

def CleanStandsDataset(df):
    df[['GO1','GO2','GO3','GO4','GO5','GO6','GO7']]=df.Accessed_by_Gates.str.split(',',expand=True)
    #Unpivoting using Melt function
    df_unpivoted = df.melt(id_vars=['Stand','Requires_Bus','Accessed_by_Gates'], var_name='GO', value_name='Gate')
    #drop columns
    df_unpivoted=df_unpivoted.drop(['Accessed_by_Gates'],axis=1)
    df_unpivoted=df_unpivoted.drop(['GO'],axis=1)
    #Removing all nulls in the Gate Column
    df=df_unpivoted.dropna(subset=['Gate'], how='all') 

    return(df)

def get_output_schema():
    return pd.DataFrame({
            'Stand' : prep_string(),
            'Requires_Bus' :  prep_string(),
            'Gate' : prep_string(),

})