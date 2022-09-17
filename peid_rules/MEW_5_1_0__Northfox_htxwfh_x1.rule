rule _MEW_5_1_0__Northfox_htxwfh
{
	meta:
		description = "MEW 5 1_0 __ Northfox"
	strings:
		$a = {BE5B004000AD91AD9353AD96565FACC0C0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
