package workers;

import exception.EmptyInput;
import exception.MinBasePay;
import exception.MonthlyBonous;
import exception.SpecialBnonus;
import exception.ValidGender;

public class Algorithmists extends Software_Developer {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private int SpecialBnonus;
	
	public Algorithmists(int ID, String FirstName, String LastName, String PhoneNum, String Email,Gender gender,int Basepay, int MonthlyBonus,int Bonous) throws ValidGender, MinBasePay, MonthlyBonous, SpecialBnonus, EmptyInput {
		super(ID, FirstName, LastName, PhoneNum, Email,gender,Basepay, MonthlyBonus);
		setBonous(SpecialBnonus);
}
	public Algorithmists(int ID, String FirstName, String LastName, String PhoneNum, String Email,Gender gender,int BasePay,int MonthlyBonus) throws ValidGender, MinBasePay, MonthlyBonous, EmptyInput {
		super(ID, FirstName, LastName, PhoneNum, Email,gender,BasePay,MonthlyBonus);
		this.SpecialBnonus = 0;
	}
	
	

	public int getBonous() {
		return this.SpecialBnonus;
	}

	public void setBonous(int Bonous) throws SpecialBnonus {
		if(Bonous >= 0)
			this.SpecialBnonus = Bonous;
		else
			throw new SpecialBnonus();
	}
	@Override
	public int Salary() {
		return super.Salary() + this.getBonous();
	}
	
	
	
	
	
	
	
}