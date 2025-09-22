from sqlalchemy import Column, String, DateTime, JSON, Boolean, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    company_name = Column(String)
    created_at = Column(DateTime, default=datetime.now)

class ContentCampaign(Base):
    __tablename__ = 'content_campaigns'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    description = Column(Text)
    platform = Column(String)
    tone = Column(String)
    target_audience = Column(String)
    created_at = Column(DateTime, default=datetime.now)



class GenerateContent(Base):
    __tablename__ = 'generate_content'

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey('content_campaigns.id'))
    content_type = Column(String)
    content_text = Column(Text)
    metadata = Column(JSON)
    generate_at  = Column(DateTime, default=datetime.now)
    is_approved = Column(Boolean, default=False)

    