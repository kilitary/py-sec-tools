rule _Thinstall_Embedded_2_620_2_623__Jitit_ewckpp
{
	meta:
		description = "Thinstall Embedded 2_620_2_623 __ Jitit"
	strings:
		$a = {E80000000058BBAC1E00002BC35068????????68B021000068C4000000E8C3FEFFFFE999FFFFFF0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
