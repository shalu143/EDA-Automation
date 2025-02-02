import pandas as pd

class HandleNull(object):
    def __init__(self,*arg,**kwarg):
        """parameters refering to drop percentage in rows and columns"""
        self.drop_percent_row = 0.3
        self.drop_percent_col = 0.4
    
    def drop_rows(self,df,**kwargs):
        """Drops rows having drop_percent_row fraction of null values"""
        
        #Setting the parameters
        if 'drop_percent' in kwargs:
            self.drop_percent_row = kwargs['drop_percent']
            assert self.drop_percent_row<1 and self.drop_percent_row > 0, 'Drop Percentage must be a fraction'
            
        if 'columns' in kwargs:
            df.dropna(subset=kwargs['columns'],axis=0,inplace = True)
            return
        
        #Interacting with user
        drop = 'change'
        from math import ceil
        drop_percent = self.drop_percent_row
        while drop=='change':
            print('Rows having more than ',drop_percent*100,'%',' null values are dropped')
            num_rows_dropped = df.shape[0]-df.dropna(axis=0,how='any',thresh=df.shape[1]-ceil(drop_percent*df.shape[1])).shape[0]
            print('Number of rows to be dropped: ',num_rows_dropped)
            drop = input('Please type yes or no to drop rows, To change the percentage please type "change": ')
            if drop == 'change':
                drop_percent = float(input('Enter percentage(0-1): '))
            elif drop=='no':
                return
            elif drop=="yes":
                df.dropna(axis=0,how='any',thresh=df.shape[1]-ceil(drop_percent*df.shape[1]),inplace=True) 
            else:
                print("please Enter yes, no or change only")
                self.drop_rows(df)
                
         
            
        #Dropping the rows   
        

    def drop_cols(self,df,**kwargs):
        """Drop columns having drop_percent_col fraction of null values"""
        #setting the parameters
        if 'drop_percent' in kwargs:
            self.drop_percent_col = kwargs['drop_percent']
        drop_percent = self.drop_percent_col
        
        #handling user input
        drop = 'change'
        columns_dropped = []
        while drop=='change':
            print('Columns having more than ',drop_percent*100,'%',' null values are dropped')
            for column in df.columns.values:
                fraction = df[column].isna().sum()/df.shape[0]
                if fraction > drop_percent:
                    columns_dropped.append(column)
            print(columns_dropped)
            drop = input('Please type yes or no to drop columns, To change the percentage please type "change": ')
            if drop == 'change':
                drop_percent = float(input('Enter percentage(0-1): '))
                columns_dropped = []
            elif drop=='no':
                return
            elif drop=="yes":
                df.drop(columns_dropped,axis=1,inplace=True)
                print('The Dropped Columns are ',columns_dropped)
                return columns_dropped
            else:
                print("please Enter yes, no or change only")
                self.drop_cols(df)
                
        
        #Dropping columns
        