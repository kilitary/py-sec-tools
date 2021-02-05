rule _ASPack_v1_08_03_zoqyat
{
	meta:
		description = "ASPack v1_08_03"
	strings:
		$a = {60E8000000005D????????????BB????????03DD2B9DB150440083BDAC50440000899DBB4E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
