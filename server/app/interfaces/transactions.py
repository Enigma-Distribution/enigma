from uuid import uuid4
from app.datastore import transactions as transactions_db


def insert_transaction(data):
    
    transaction = {
        "transaction_id": str(uuid4()), 
        "transaction_type": data["transaction_type"], 
        "amount": data["amount"], 
        "worker_id": data["worker_id"], 
        "step_id": data["step_id"], 
        "phase": data["phase"], 
        "result_file_id": data["result_file_id"],
        "efficiency": data["efficiency"]
    }
    print("Calling db's transaction insert method") 
    transactions_db.insert_transaction(transaction)