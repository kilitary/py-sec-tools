rule _eXPressor_1_1__CGSoftLabs_vknfij
{
	meta:
		description = "eXPressor 1_1 __ CGSoftLabs"
	strings:
		$a = {E9????0000E9????0000E9??120000E9??0C0000E9????0000E9????0000E9????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
