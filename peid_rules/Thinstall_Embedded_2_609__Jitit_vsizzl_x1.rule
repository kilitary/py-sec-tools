rule _Thinstall_Embedded_2_609__Jitit_vsizzl
{
	meta:
		description = "Thinstall Embedded 2_609 __ Jitit"
	strings:
		$a = {E80000000058BBAD1900002BC35068????????68B01C00006880000000E835FFFFFFE999FFFFFF00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
