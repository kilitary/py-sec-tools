rule _Setup_Factory_6_x_Custom_nhpsuv
{
	meta:
		description = "Setup Factory 6_x Custom"
	strings:
		$a = {558BEC6AFF68??61400068??43400064A100000000506489250000000083EC585356578965E8FF15??61400033D28AD48915A0A940008BC881E1FF000000890D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
