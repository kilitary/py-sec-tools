rule _DEF_v1_0_cqvvqh
{
	meta:
		description = "DEF v1_0"
	strings:
		$a = {BE??0140006A??59807E070074118B460C05000040008B56103010404A75FA83C628E2E468??104000C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
