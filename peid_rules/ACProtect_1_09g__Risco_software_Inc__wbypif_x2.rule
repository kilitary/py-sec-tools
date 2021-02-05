rule _ACProtect_1_09g__Risco_software_Inc__wbypif
{
	meta:
		description = "ACProtect 1_09g __ Risco software Inc_"
	strings:
		$a = {60EB??5DEB??FF??????????E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
