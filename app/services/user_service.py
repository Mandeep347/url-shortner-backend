from app.repositories.user_repository import UserRepository

repository = UserRepository()

class UserService:

    def create_user(self, db, user_data):
        user = repository.create(
            db, user_data.username, user_data.email
        )

        db.commit()
        db.refresh(user)
    
    def get_user(self, db):
        return repository.get_all(db)
    
    def get_user_by_id(self, db, id):
        return repository.get_by_id(db, id)
    
    def update_user(self, db, id, user_data):
        return repository.update_user(
            db, id, user_data.username, user_data.email
        )
    
    def delete_user(self, db, id):
        return repository.delete_user(db, id)