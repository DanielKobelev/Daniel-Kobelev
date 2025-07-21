package exception;

public class EmployeeDoesntExist extends Exception {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public EmployeeDoesntExist() {
		
	}
		public EmployeeDoesntExist(String msg) {
			super(msg);
}}
