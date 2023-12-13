from app import db  # Assurez-vous d'importer votre instance de base de données SQLAlchemy

def count_records_in_tables():
    try:
        table_records = {}
        metadata = db.metadata

        for table in metadata.tables.values():
            table_name = table.name
            record_count = db.session.query(table).count()
            table_records[table_name] = record_count

        return table_records

    except Exception as e:
        return f"Une erreur s'est produite : {e}"
