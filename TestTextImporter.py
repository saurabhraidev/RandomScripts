import pandas as pd


class TestTextImporter:
    
    
    def __init__(self):
        
        self.data = pd.read_csv('Data/oasst1-train.csv')
        self.import_text_size = 0
        self.column_name = "text"
        self.output_text = ""
    
    def get_output(self, number_of_texts_to_import: int) -> str:
        self.import_text_size  = number_of_texts_to_import
        for i in range(self.import_text_size):
            self.output_text += self.data[self.column_name][i]
        return self.output_text
