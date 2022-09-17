rule __NET_executable__Microsoft_ljrgym
{
	meta:
		description = "_NET executable __ Microsoft"
	strings:
		$a = {00000000000000005F436F724578654D61696E006D73636F7265652E646C6C0000000000FF25}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
