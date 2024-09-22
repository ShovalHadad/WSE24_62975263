﻿using Microsoft.EntityFrameworkCore;
using WebApp.models;
using WebApp.Models;


namespace WebApp.Data
{
    public class ApplicationDBContext : DbContext
    {
        public ApplicationDBContext(DbContextOptions dbContextOptions) : base(dbContextOptions) {} // empty constractor
        // add the tables in the data base:
        public DbSet<Flight> Flights { get; set; }
        public DbSet<Plane> Planes { get; set; }
        public DbSet<FrequentFlyer> FrequentFlyers { get; set; }
        public DbSet<FlightTicket> FlightTickets { get; set; }

    }
}
