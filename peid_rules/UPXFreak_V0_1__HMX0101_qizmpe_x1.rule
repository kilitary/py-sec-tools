rule _UPXFreak_V0_1__HMX0101_qizmpe
{
	meta:
		description = "UPXFreak V0_1 __ HMX0101"
	strings:
		$a = {BE????????83C601FFE60000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
