import os

# Define a custom domain exception inheriting from the base Exception class
class PipelineExecutionError(Exception):
    """Raised when critical operational anomalies compromise the pipeline execution."""
    pass

class FileDataTransformer:
    def __init__(self, source_path):
        self.source_path = source_path
        self.file_handle = None

    def read_and_convert(self):
        print(f"Opening system data stream at: {self.source_path}")
        
        try:
            # Dangerous step: File might not exist
            if not os.path.exists(self.source_path):
                raise FileNotFoundError(f"Target file missing at path context: {self.source_path}")
                
            self.file_handle = open(self.source_path, 'r')
            raw_content = self.file_handle.read()
            
            # Dangerous step: File might be empty or corrupted text
            if len(raw_content.strip()) == 0:
                raise ValueError("Source file stream contains zero readable content.")
                
            # Simulate processing string to integers
            processed_numeric = int(raw_content.strip())
            return processed_numeric

        except FileNotFoundError as fnf_err:
            print(f"[LOG LEVEL - WARN]: Handled structural error: {fnf_err}")
            # Reraise a clean custom error so orchestrators can handle it uniformly
            raise PipelineExecutionError("Data ingestion stage dropped: File not found.") from fnf_err
            
        except ValueError as val_err:
            print(f"[LOG LEVEL - CRIT]: Handled mutation error: {val_err}")
            raise PipelineExecutionError("Data transformation stage dropped: Conversion error.") from val_err
            
        except Exception as generic_err:
            print(f"[LOG LEVEL - UNKNOWN]: Unknown system catch: {generic_err}")
            raise PipelineExecutionError("Fatal pipeline runtime drop.") from generic_err
            
        finally:
            # THIS CODE ALWAYS EXECUTES REGARDLESS OF THE EXCEPTION ABOVE
            # Vital in data engineering to close database locks and file handlers safely
            if self.file_handle and not self.file_handle.closed:
                print("Closing data stream handle safely via finally routine.")
                self.file_handle.close()


# ---- RUNNING TEST BENCH ----
if __name__ == "__main__":
    # Test 1: Let's create an empty corrupted file to trigger our validation
    corrupted_file_path = "corrupted_market_log.txt"
    with open(corrupted_file_path, "w") as f:
        f.write("") # Writing nothing to induce ValueError
        
    transformer = FileDataTransformer(corrupted_file_path)
    
    try:
        transformer.read_and_convert()
    except PipelineExecutionError as p_err:
        print(f"\nCaught custom application exception: {p_err}")
        
    # Clean up file post-run
    if os.path.exists(corrupted_file_path):
        os.remove(corrupted_file_path)