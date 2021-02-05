rule _ASProtect_1_33__2_1_Registered__Alexey_Solodovnikov_yaedur
{
	meta:
		description = "ASProtect 1_33 _ 2_1 Registered __ Alexey Solodovnikov"
	strings:
		$a = {6801??????E801000000C3C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
