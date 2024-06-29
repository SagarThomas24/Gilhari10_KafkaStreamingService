package javasrcDB1.src.main.java.models;

import org.json.JSONException;
import org.json.JSONObject;

import com.softwaretree.jdx.JDX_JSONObject;

public class JSON_Buyer extends JDX_JSONObject {
    public JSON_Buyer() {         
        super();     
    }      
    public JSON_Buyer(JSONObject jsonObject) throws JSONException {         
        super(jsonObject);     
    } 
} 
