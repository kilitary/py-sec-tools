rule _Thinstall_vx_x_dcctmx
{
	meta:
		description = "Thinstall vx_x"
	strings:
		$a = {9C60685374416C685468496EE80000000058BB????????2BC35068????????68????????68????????E82CFFFFFFE990FFFFFFCCCC558BEC83C4F4FC5357568B75088B7D0CC745FC0800000033DBBA000000804333}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
