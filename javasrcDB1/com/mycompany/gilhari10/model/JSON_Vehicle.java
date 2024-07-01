package javasrcDB1.src.main.java.models;

import org.json.JSONException;
import org.json.JSONObject;

import com.softwaretree.jdx.JDX_JSONObject;

public class JSON_Vehicle extends JDX_JSONObject {
    public JSON_Vehicle() {         
        super();     
    }      
    public JSON_Vehicle(JSONObject jsonObject) throws JSONException {         
        super(jsonObject);     
    } 
} 
