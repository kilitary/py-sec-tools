rule _ExeTools_COM2EXE_eysjoe
{
	meta:
		description = "ExeTools COM2EXE"
	strings:
		$a = {E8????5D83ED??8CDA2E8996????83C2??8EDA8EC22E0196????60}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
