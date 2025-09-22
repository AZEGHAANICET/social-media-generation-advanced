
from app.utils.parsers import post_generate_schema_parser
def post_prompt(count, topic, platform):
    prompt = f"""
       Generate exactly {count} engaging post ideas about {topic} for {platform}.

       Return ONLY a valid JSON array with exactly {count} objects (no extra text).
       Each object must contain:
         - "title": string
         - "key_points": string
         - "visual_elements": string
       Example:
            [
                  {{
                    "title": "Example title",
                    "key_points": ["key1", "key2"],
                    "visual_elements": "visual suggestions"
                  }},
                  {{
                    "title": "Example title",
                    "key_points": ["key1", "key2"],
                    "visual_elements": "visual suggestions"
                  }}
            ]
    """
    return prompt


def hashtags_prompt(count, platform, content):
    prompt = f"""
        Generate {count} relevant hashtags for this content on {platform}
        {content}
        Return only the hashtags as a comma-separated list.        
        """
    return prompt

def caption_prompt(platform, tone, max_length):
    prompt = f"""
        You are a professional social media content creator specializing in {platform}
        create engaging content with a {tone} tone.
        Maximum length must be : {max_length} characters
        """
    return prompt
