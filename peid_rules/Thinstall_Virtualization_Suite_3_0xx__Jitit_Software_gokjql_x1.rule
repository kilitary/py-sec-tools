rule _Thinstall_Virtualization_Suite_3_0xx__Jitit_Software_gokjql
{
	meta:
		description = "Thinstall Virtualization Suite 3_0xx __ Jitit Software"
	strings:
		$a = {9C60685374416C685468496EE80000000058BB371F00002BC35068000000016800??00006804010000E8BAFEFFFFE990FFFFFFCCCCCCCCCCCCCC558BEC83C4F4}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
