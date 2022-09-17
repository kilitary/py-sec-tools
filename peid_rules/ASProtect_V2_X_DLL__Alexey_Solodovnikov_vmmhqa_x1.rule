rule _ASProtect_V2_X_DLL__Alexey_Solodovnikov_vmmhqa
{
	meta:
		description = "ASProtect V2_X DLL __ Alexey Solodovnikov"
	strings:
		$a = {60E803000000E9????5D4555C3E801000000EB5DBB????????03DD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
