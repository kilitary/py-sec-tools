rule _Thinstall_Virtualization_Suite_V3_10X__Thinstall_Company_lraiif
{
	meta:
		description = "Thinstall Virtualization Suite V3_10X __ Thinstall Company"
	strings:
		$a = {9C60685374416C685468496EE80000000058BB????????2BC35068????????68????????68????????E82CFFFFFFE990FFFFFFCCCC558BEC83C4F4FC5357568B75088B7D0CC745FC0800000033DBBA000000804333C0E819010000730E8B4DF8E8270100000245F7AAEBE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
