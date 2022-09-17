rule _StarForce_V3_X_DLL__StarForce_Copy_Protection_System_gqorpq
{
	meta:
		description = "StarForce V3_X DLL __ StarForce Copy Protection System"
	strings:
		$a = {E8??????5E83EE??B8CF7BCD213DCF7B????0E1F81C6????BF????B9????FCF3A4061F06B8????50CBB448BB2C00CD21}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
