rule _HPA_iyxgpj
{
	meta:
		description = "HPA"
	strings:
		$a = {E8????5E8BD683????83????060E1E0E1F33FF8CD3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
