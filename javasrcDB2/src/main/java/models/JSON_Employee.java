package javasrcDB2.src.main.java.models;

import org.json.JSONException;
import org.json.JSONObject;

import com.softwaretree.jdx.JDX_JSONObject;

public class JSON_Employee extends JDX_JSONObject {
    public JSON_Employee() {         
        super();     
    }      
    public JSON_Employee(JSONObject jsonObject) throws JSONException {         
        super(jsonObject);     
    } 
} 
