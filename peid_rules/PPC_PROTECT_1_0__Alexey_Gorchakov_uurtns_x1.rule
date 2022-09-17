rule _PPC_PROTECT_1_0__Alexey_Gorchakov_uurtns
{
	meta:
		description = "PPC_PROTECT 1_0 __ Alexey Gorchakov"
	strings:
		$a = {FF5F2DE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
