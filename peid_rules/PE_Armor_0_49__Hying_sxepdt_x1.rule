rule _PE_Armor_0_49__Hying_sxepdt
{
	meta:
		description = "PE_Armor 0_49 __ Hying"
	strings:
		$a = {5652515355E81501000032????0000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
