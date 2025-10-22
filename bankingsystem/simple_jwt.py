import base64
import json
import datetime

class SimpleJWT:
    SECRET_KEY = "banking_secret_2024"
    
    @classmethod
    def create_admin_token(cls, user_id: str) -> str:
        """Tạo token đơn giản cho Admin (15 phút)"""
        payload = {
            "user_id": user_id,
            "role": "Admin",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
        }
        
        # Encode payload
        payload_json = json.dumps(payload, default=str)
        payload_b64 = base64.b64encode(payload_json.encode()).decode()
        
        # Tạo signature đơn giản
        signature = base64.b64encode(f"{payload_b64}.{cls.SECRET_KEY}".encode()).decode()
        
        return f"{payload_b64}.{signature}"
    
    @classmethod
    def verify_token(cls, token: str) -> bool:
        """Kiểm tra token có hợp lệ không"""
        if not token:
            return False
        
        try:
            parts = token.split('.')
            if len(parts) != 2:
                return False
            
            payload_b64, signature = parts
            
            # Verify signature
            expected_signature = base64.b64encode(f"{payload_b64}.{cls.SECRET_KEY}".encode()).decode()
            if signature != expected_signature:
                return False
            
            # Decode payload
            payload_json = base64.b64decode(payload_b64).decode()
            payload = json.loads(payload_json)
            
            # Check expiration
            exp = datetime.datetime.fromisoformat(payload['exp'])
            if datetime.datetime.utcnow() > exp:
                return False
            
            return True
            
        except:
            return False
    
    @classmethod
    def is_admin(cls, token: str) -> bool:
        """Kiểm tra có phải Admin không"""
        return cls.verify_token(token)

# Demo sử dụng
if __name__ == "__main__":
    # Tạo admin token
    admin_token = SimpleJWT.create_admin_token("admin001")
    print(f"Admin token: {admin_token}")
    
