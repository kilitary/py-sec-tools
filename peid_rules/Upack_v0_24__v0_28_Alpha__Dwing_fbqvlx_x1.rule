rule _Upack_v0_24__v0_28_Alpha__Dwing_fbqvlx
{
	meta:
		description = "Upack v0_24 _ v0_28 Alpha __ Dwing"
	strings:
		$a = {BE88014000AD????95AD91F3A5AD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
