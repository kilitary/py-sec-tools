rule _TAV_rfmllx
{
	meta:
		description = "TAV"
	strings:
		$a = {E8????4D5ACB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
