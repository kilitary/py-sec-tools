rule _DrWeb_v4_00_Virus_DataBase_ozwren
{
	meta:
		description = "DrWeb v4_00_ Virus DataBase"
	strings:
		$a = {49445257}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
