rule _MEW_5_1_0__Northfox_ucfaiv
{
	meta:
		description = "MEW 5 1_0 __ Northfox"
	strings:
		$a = {BE4801??????????95A533C0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
