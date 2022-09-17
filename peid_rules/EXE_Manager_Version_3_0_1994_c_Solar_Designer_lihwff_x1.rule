rule _EXE_Manager_Version_3_0_1994_c_Solar_Designer_lihwff
{
	meta:
		description = "EXE Manager Version 3_0 1994 _c_ Solar Designer"
	strings:
		$a = {B4301E06CD212E??????BF????B9????33C02E????47E2}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
