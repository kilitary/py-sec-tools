rule _Thinstall_Virtualization_Suite_3_049_3_080__Thinstall_Company_jrigeq
{
	meta:
		description = "Thinstall Virtualization Suite 3_049_3_080 __ Thinstall Company"
	strings:
		$a = {9C60685374416C685468496EE80000000058BB371F00002BC35068????????68002C00006804010000E8BAFEFFFFE990FFFFFFCCCCCCCCCCCCCC558BEC83C4F4FC5357568B75088B7D0CC745FC0800000033DBBA00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
