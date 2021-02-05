rule _ACProtect_v1_90g__Risco_software_Inc__eokzsi
{
	meta:
		description = "ACProtect v1_90g __ Risco software Inc_"
	strings:
		$a = {600F87020000001BF8E8010000007383042406C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
