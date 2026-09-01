from dataclasses import dataclass

@dataclass         #Data class is basically a c;ass where u can simply define the variable names
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str
    
