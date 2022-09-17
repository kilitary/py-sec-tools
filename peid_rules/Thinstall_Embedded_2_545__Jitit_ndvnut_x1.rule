rule _Thinstall_Embedded_2_545__Jitit_ndvnut
{
	meta:
		description = "Thinstall Embedded 2_545 __ Jitit"
	strings:
		$a = {E8F2FFFFFF5068????????68401B0000E842FFFFFFE99DFFFFFF000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
