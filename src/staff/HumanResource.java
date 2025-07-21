package staff;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import exception.EmployeeDoesntExist;
import exception.Existing_Employee;
import workers.Employee;

public class HumanResource implements Serializable {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private ArrayList<Employee> List;

	
	public HumanResource(ArrayList<Employee>List){
		this.List = List;
		Collections.sort(List);}
		
	
	public void AddEmployee(Employee other) throws Existing_Employee {
		for(Employee X:List) {
			if(X.getID() == other.getID()){
				throw new Existing_Employee("Employee already exist in our data base  ");}}
			List.add(other);}
			
		
	
		
	
	public Employee FindEmployeeById(int id) throws EmployeeDoesntExist  {
		for(Employee x:List) {
			if(x.getID() == id) {
				return x;}}
		throw new EmployeeDoesntExist("Employee doest not exist in our data base  ");}
				
			
				
	
	public void DeletEmployeeByiD(int id) throws EmployeeDoesntExist {
		for(Employee x : List) {
	        if (x.getID() == id) {
	            List.remove(x);
	            return;
	        }
	    }
			throw new EmployeeDoesntExist("Employee doest not exist in our data base 3  ");}
	
	

	
		@Override
		public String toString() {
			Collections.sort(List);
			String str = "Our workers\n\n";
			for(Employee x:List)
				str += x +"\n";
			return str;
			
		
	
	
	
}
	
}
		
		
		
	
	
				
		
		
		
		
		
	
