package workers;

import exception.EmptyInput;
import exception.MinBasePay;
import exception.MonthlyBonous;
import exception.ValidGender;

public class Software_Developer extends Employee{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private int MonthlyBonus;
	
	public Software_Developer(int ID, String FirstName, String LastName, String PhoneNum, String Email,Gender gender,int Basepay,int MonthlyBonus) throws ValidGender, MinBasePay, MonthlyBonous, EmptyInput {
		super(ID, FirstName, LastName, PhoneNum, Email,gender,Basepay);
		setMonthlyBonus(MonthlyBonus);
    }
	public Software_Developer(int ID, String FirstName, String LastName, String PhoneNum, String Email,Gender gender,int Basepay) throws ValidGender, MinBasePay, EmptyInput{
		super(ID, FirstName, LastName, PhoneNum, Email,gender,Basepay);
		this.MonthlyBonus = 0;}

	public int getMonthlyBonus() {
		return MonthlyBonus;
	}

	public void setMonthlyBonus(int MonthlyBonus) throws MonthlyBonous {
		if(MonthlyBonus >= 0)
			this.MonthlyBonus = MonthlyBonus;
		else
			throw new MonthlyBonous();
	}

	@Override
	public int Salary() {
		return super.Salary() + this.getMonthlyBonus();
	}
	@Override
	public String toString() {
		return super.toString() 
				+ "[His monthly salary is: "
				+ Salary()
				+"]";
		
	}

}
