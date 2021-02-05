rule _TAV_ivetmp
{
	meta:
		description = "TAV"
	strings:
		$a = {E8????4D5ACB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
