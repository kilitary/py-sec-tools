rule __NET_DLL__Microsoft_ieidup
{
	meta:
		description = "_NET DLL __ Microsoft"
	strings:
		$a = {00000000000000005F436F72446C6C4D61696E006D73636F7265652E646C6C0000??0000FF25}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
