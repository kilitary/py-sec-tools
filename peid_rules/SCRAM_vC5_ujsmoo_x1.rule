rule _SCRAM_vC5_ujsmoo
{
	meta:
		description = "SCRAM_ vC5"
	strings:
		$a = {B8????509D9C5825????75??BA????B409CD21CD20}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
